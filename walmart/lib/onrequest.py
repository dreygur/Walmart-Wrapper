import os 
from pathlib import Path
import json
import pandas as pd
from datetime import datetime
from typing import Dict, List, Union, Tuple, Optional


# LOCAL IMPORTS
from walmart.core import Resource


# Assets
today:str       = datetime.now().strftime(r"%Y-%m-%d")

class ONRequest(Resource):
    """ ON Request EndPoints """

    path:str = 'reports'

    def send_report(self,report_type:str)->str:
        """ Generate Report: """

        url:str = 'reportRequests/'
        response:dict  = self.connection.send_request( 
                                method = 'POST',
                                url    = "{}/{}".format(self.url,url),
                                params = {  "reportType"   : report_type, "reportVersion": 'v1', "requestStatus": "READY" }
                            )
            
        if 'requestId' in response.keys():
            filename:str = str(os.path.join(os.getcwd(),'reports',"{}_report_{}.json".format(report_type,today)) ) 
            report_obj   = json.dumps(response)
            # Writing into JSON 
            with open(file=filename,mode='w') as outfile:
                outfile.write(report_obj)
            return "file saved as: {}".format(filename)
    
    
    def report_status(self,report_type:str,file_path:str=None)->str:
        """ Check Status Report """

        url:str                         = "reportRequests/"
        if file_path is None: file:str  = str(os.path.join(os.getcwd(),'reports',"{}_report_{}.json".format(report_type,today)) ) 
        else: file:str                  = file_path

        if os.path.isfile(file):
            with open( file, 'r' ) as outfile: json_file :dict = json.load(outfile)
            request_id = json_file['requestId']
            res = self.connection.send_request(
                                    method = 'GET',
                                    url    = "{}/{}/{}".format(self.url,url,request_id) 
                                    )
            return res['requestStatus']
        else:
            raise ValueError("Missing Expected File: {}".format(file))
    
    def download_report(self,report_type:str,file_path:str=None)->str:
        """Download report"""

        url:str  = 'downloadReport/'
        if file_path is None: file:str     = str(os.path.join(os.getcwd(),'reports',"{}_report_{}.json".format(report_type,today)) ) 
        else: file:str     = file_path 
            
        if os.path.isfile(file):
            with open(file,'r') as outfile: json_file:dict = json.load(outfile)
            request_id = json_file['requestId']
            res = self.connection.send_request(
                                        method = "GET",
                                        url    = "{}/{}".format(self.url,url),
                                        params = { 'requestId':request_id}
                                    )
            df:pd.DataFrame         = pd.read_csv(res['downloadURL'], compression='zip')
            csv_file_name:str       = os.path.join( Path(file).parent, "{}_report_{}.csv".format(report_type,today))
            df.assign(reqSubmissionDate=res['requestSubmissionDate']).to_csv(path_or_buf=csv_file_name,index=False)
            return "Downloaded 🥂!!"
        else:
            raise ValueError("Missing Expected File: {}".format(file))