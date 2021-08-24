# -*- coding: utf-8 -*-
# IMPORTS
import os
import io
import csv
import zipfile
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from walmart.core import Resource

class Report(Resource):
  """
  Get report
  """

  path = 'getReport'

  @property
  def available(self) -> List[Dict]:
    url = '/report/reconreport/availableReconFiles'
    return self.connection.send_request(
        method='GET',
        url=self.connection.base_url + url,
    )

  def recon_report(
    self,
    date: str
  ) -> Union[Dict, List]:
    url = '/report/reconreport/reconFile'
    zippedfile = self.connection.send_request(
        method='GET',
        url=self.connection.base_url + url,
        params={"reportDate": date},
    )

    zf = zipfile.ZipFile(io.BytesIO(zippedfile), "r")
    product_report = zf.read(zf.infolist()[0]).decode("utf-8")

    return list(csv.DictReader(io.StringIO(product_report)))

  def get_report(
    self,
    type: str
  ) -> Union[Dict, List]:
    """
    Types:
      - "item"
      - "buybox"
      - "cpa"
      - "shippingProgram"
      - "shippingConfiguration"
      - "itemPerformance"
      - "returnOverrides"
      - "promo"
    """
    zippedfile = self.connection.send_request(
        method='GET',
        url=self.url,
        params={"type": type},
    )

    zf = zipfile.ZipFile(io.BytesIO(zippedfile), "r")
    product_report = zf.read(zf.infolist()[0]).decode("utf-8")

    return list(csv.DictReader(io.StringIO(product_report)))
