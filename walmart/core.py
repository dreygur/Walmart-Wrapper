# -*- coding: utf-8 -*-
# IMPORTS
from lxml.builder import E, ElementMaker
from lxml import etree
from requests.auth import HTTPBasicAuth
from datetime import datetime
import uuid
import requests
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from .exceptions import WalmartAuthenticationError

class Core(object):
  def __init__(
    self,
    client_id: str,
    client_secret: str
  ) -> object:
    """To get client_id and client_secret for your Walmart Marketplace
    visit: https://developer.walmart.com/#/generateKey
    """
    self.client_id = client_id
    self.client_secret = client_secret
    self.token = None
    self.token_expires_in = None
    self.base_url = "https://marketplace.walmartapis.com/v3"
    # self.base_url = "https://sandbox.walmartapis.com/v3"

    session = requests.Session()
    session.headers.update({
      "WM_SVC.NAME": "Walmart Marketplace",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json",
    })
    session.auth = HTTPBasicAuth(self.client_id, self.client_secret)
    self.session = session

    # Get the token required for API requests
    self.authenticate()

  def authenticate(self):
    data = self.send_request(
      "POST", "{}/token".format(self.base_url),
      body={
        "grant_type": "client_credentials",
      },
    )
    self.token = data["access_token"]
    self.token_expires_in = data["expires_in"]

    self.session.headers["WM_SEC.ACCESS_TOKEN"] = self.token

  def send_request(
    self,
    method: str,
    url: str,
    params: Dict = None,
    body: Dict = None,
    json: Dict = None,
    request_headers: Dict = None
  ):
    # A unique ID which identifies each API call and used to track
    # and debug issues; use a random generated GUID for this ID
    headers = {
      "WM_QOS.CORRELATION_ID": uuid.uuid4().hex,
    }
    if request_headers:
      headers.update(request_headers)

    response = None
    if method == "GET":
      response = self.session.get(url, params=params, headers=headers)
    elif method == "PUT":
      response = self.session.put(
        url, params=params, headers=headers, data=body
      )
    elif method == "POST":
      request_params = {
        "params": params,
        "headers": headers,
      }
      if json is not None:
        request_params["json"] = json
      else:
        request_params["data"] = body
      response = self.session.post(url, **request_params)

    if response is not None:
      try:
        response.raise_for_status()
      except requests.exceptions.HTTPError:
        if response.status_code == 401:
          raise WalmartAuthenticationError((
            "Invalid client_id or client_secret. Please verify "
            "your credentials from https://developer.walmart."
            "com/#/generateKey"
          ))
        elif response.status_code == 400:
          data = response.json()
          if "error" in data and data["error"][0]["code"] == \
                "INVALID_TOKEN.GMP_GATEWAY_API":
            # Refresh the token as the current token has expired
            self.authenticate()
            return self.send_request(
              method, url, params, body, request_headers
            )
        raise
    try:
      return response.json()
    except ValueError:
      # In case of reports, there is no JSON response, so return the
      # content instead which contains the actual report
      return response.content

class Resource(object):
  """
  A base class for all Resources to extend
  """

  def __init__(self, connection):
    self.connection = connection

  @property
  def url(self):
    return "{}/{}".format(self.connection.base_url, self.path)

  def all(self, **kwargs):
    return self.connection.send_request(
      method="GET", url=self.url, params=kwargs
    )

  def get(self, id):
    url = "{}/{}".format(self.url, id)
    return self.connection.send_request(method="GET", url=url)

  def update(self, **kwargs):
    return self.connection.send_request(
      method="PUT", url=self.url, params=kwargs
    )
