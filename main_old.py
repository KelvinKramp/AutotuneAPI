from flask import Flask
from flask_restful import Api, Resource, reqparse
import subprocess
from get_profile import get_profile
import os
import shutil
from ROOT_DIR import ROOT_DIR, checkdir
import sys


app = Flask(__name__)
api = Api(app)


get_args = reqparse.RequestParser()
get_args.add_argument("--nightscout", type=str, help="Nightscout URL. Required. ", required=True)
get_args.add_argument("--start-date", type=str, help="Start date YYYY-MM-DD. Required. ", required=True)
get_args.add_argument("--end-date", type=str, help="End date YYYY-MM-DD, Not required. Will be set as today if not given.", required=False)
get_args.add_argument("--token", type=str, help="Authenticaton token. Not required. ", required=False)

home=os.path.expanduser('~')


class API_class(Resource):
	def get(self, step):
		args = get_args.parse_args()
		nightscout = args["--nightscout"]
		# get method for profile
		if step == "get-profile":
			get_profile(nightscout)
			print("nightscout profile succesfully retreived")
			return 200

	# get method for autotune result
		elif step == "run-autotune":
			args = get_args.parse_args()
			nightscout = args["--nightscout"]
			token = args["--token"]
			start_date = args["--start-date"]
			end_date = args["--end-date"]
			# print(nightscout)
			# print(token)
			# print(start_date)
			# print(end_date)
			if not 'end_date':
				from datetime import datetime as dt
				end_date = dt.utcnow().date().strftime("%Y-%m-%d")

			# *** I INCLUDED THIS PART WHEN TRYING TO RUN ON EPIPHMERIAL GCP, IF RUN ON LOCAL THIS IS NOT NECESSARY
			# BUT INSTEAD RUN https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html from step 1c
			# command1 = "./install.sh"
			# os.chdir(ROOT_DIR)
			# subprocess.call(command1, shell=True)

			myopenaps = "/myopenaps"
			myopenaps = ROOT_DIR + myopenaps
			checkdir(myopenaps)
			command2 = "oref0-autotune --dir={} --ns-host={} --start-date={}  --end-date={} > logfile.txt".format(myopenaps, nightscout, start_date, end_date)
			subprocess.call(command2, shell=True)
			os.chdir(ROOT_DIR)
			print("new nightscout profile succesfully created and saved")
			return 200
		else:
			return 400

	# post method for switchin	g profile
	# def put(self, video_id):
	# 	args = video_put_args.parse_args()


api.add_resource(API_class, "/api/<string:step>")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)