# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from walmart.core import Resource

class Insights(Resource):
  """Insights Endpoints"""

  path = 'insights/items'

  def quality_score(
    self,
    wfs_flag: str = 'false',
    view_trending_items: bool = 'true'
  ) -> Dict:
    """Quality Score

    Args:
        wfs_flag (str, optional): [description]. Defaults to ''.
        view_trending_items (bool, optional): [description]. Defaults to True.

    Returns:
        Dict: [description]
    """
    url = 'listingQuality/score'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'wfsFlag': wfs_flag,
        'viewTrendingItems': view_trending_items
      }
    )

  def trending_items(
    self,
    department_id: str,
    category_id: str = 'null',
    limit: str = '20',
    offset: str = '0',
    timeframe: str = '7',
  ) -> Dict:
    """Trending Items

    Args:
        department_id (str): [description]
        category_id (str, optional): [description]. Defaults to 'null'.
        limit (str, optional): [description]. Defaults to '20'.
        offset (str, optional): [description]. Defaults to '0'.
        timeframe (str, optional): [description]. Defaults to '7'.

    Returns:
        Dict: [description]
    """

    url = 'trending'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'departmentId': department_id,
        'categoryId': category_id,
        'limit': limit,
        'offset': offset,
        'timeFrame': timeframe
      }
    )

  def listing_quality_issues_categories(
    self,
    wfs_flag: str = '',
    view_trending_items: bool = True,
    hass_issue: int = 0
  ) -> Dict:
    """Listing Quality Issues Categories

    Args:
        wfs_flag (str, optional): [description]. Defaults to ''.
        view_trending_items (bool, optional): [description]. Defaults to True.
        hass_issue (int, optional): [description]. Defaults to 0.

    Returns:
        Dict: [description]
    """

    url = 'listingQuality/categories'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'wfsFlag': wfs_flag,
        'viewTrendingItems': view_trending_items,
        'hasIssue': hass_issue
      }
    )

  def unpublished(
    self,
    from_date: str,
    unpublished_reason_code: str = 'all',
    limit: str = '20',
    offer_life_cycle_status: str = 'all',
    market_trending: bool = False,
    items_with_inventory: bool = True
  ) -> Dict:
    """Unpublished

    Args:
        from_date (str): [description]
        unpublished_reason_code (str, optional): [description]. Defaults to 'all'.
        limit (str, optional): [description]. Defaults to '20'.
        offer_life_cycle_status (str, optional): [description]. Defaults to 'all'.
        market_trending (bool, optional): [description]. Defaults to False.
        items_with_inventory (bool, optional): [description]. Defaults to True.

    Returns:
        Dict: [description]
    """

    url = 'unpublished/items'
    self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'fromDate': from_date,
        'unpublishedReasonCode': unpublished_reason_code,
        'limit': limit,
        'offerLifeCycleStatus': offer_life_cycle_status,
        'marketTrending': market_trending,
        'itemsWithInventory': items_with_inventory
      }
    )

  def unpublished_count(
    self,
    from_date: str,
  ) -> Dict:
    """Unpublished Count

    Args:
        from_date (str): [description]

    Returns:
        Dict: [description]
    """
    # Date Format: 2020-09-23

    url = 'unpublished/counts'
    self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'fromDate': from_date
      }
    )
