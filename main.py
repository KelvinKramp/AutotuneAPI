from flask import Flask
from flask_restful import Api, Resource, reqparse
import subprocess
from get_profile import get_profile
import os
import shutil
from ROOT_DIR import ROOT_DIR, checkdir
from get_recommendations import get_recommendations
import json
from datetime import datetime as dt

# Set variables
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
home=os.path.expanduser('~')

get_args = reqparse.RequestParser()
get_args.add_argument("--nightscout", type=str, help="Nightscout URL. Required. ", required=True)
get_args.add_argument("--start-date", type=str, help="Start date YYYY-MM-DD. Required. ", required=False)
get_args.add_argument("--end-date", type=str, help="End date YYYY-MM-DD, Not required. Will be set as today if not given.", required=False)
get_args.add_argument("--token", type=str, help="Authenticaton token. Not required. ", required=False)
get_args.add_argument("--json_profile", type=str, help="New pofile in JSON format", required=False)




class API_class(Resource):
	def get(self, step):
		args = get_args.parse_args()

		# GET PROFILE
		if step == "get-profile":
			nightscout = args["--nightscout"]
			profile = get_profile(nightscout)
			if profile:
				print("Nightscout profile succesfully retreived")
			else:
				print("nightscout profile could not be retreived")
			return profile, 200

		# RUN AUTOTUNE
		elif step == "run-autotune":
			nightscout = args["--nightscout"]
			token = args["--token"]
			start_date = args["--start-date"]
			end_date = args["--end-date"]
			try:
				if not 'end_date':
					end_date = dt.utcnow().date().strftime("%Y-%m-%d")

				# *** I INCLUDED THIS PART WHEN TRYING TO RUN ON EPIPHMERIAL GCP, IF RUN ON LOCAL THIS IS NOT NECESSARY
				# BUT INSTEAD RUN https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html from step 1c
				# command1 = "./install.sh"
				# os.chdir(ROOT_DIR)
				# subprocess.call(command1, shell=True)

				myopenaps = "/myopenaps"
				myopenaps = ROOT_DIR + myopenaps
				checkdir(myopenaps)
				print("starting autotune run")
				os.chdir(ROOT_DIR)
				command2 = "oref0-autotune --dir={} --ns-host={} --start-date={}  --end-date={}  > logfile.txt".format(myopenaps, nightscout, start_date, end_date,)
				subprocess.call(command2, shell=True)
				os.chdir(ROOT_DIR)
				print("new nightscout profile succesfully created and saved")
				print("creating recommendations file")
				command4 = "./print.sh"
				subprocess.call(command4, shell=True)
				pay_load = get_recommendations()
				print(pay_load)
				return pay_load, 200
			except Exception as e:
				return e, 500 # RETURN STATUS CODE 500 "internal server error"

		# GET RECOMMMENDATIONS
		elif step =="get-recomm":
			return "method abondend"

		# UPLOAD TO NIGTHSCOUT AND ACTIVATE
		elif step =="upload":
			nightscout = args["--nightscout"]
			profile = eval(args["--json_profile"])
			token = args["--token"]
			try:
				file_name = "/profile_2_upload.json"
				file_path = os.path.join(ROOT_DIR, UPLOAD_FOLDER, file_name)
				with open(file_path, 'w', encoding='utf-8') as f:
					json.dump(profile, f, ensure_ascii=False, indent=4)
				command4 = "oref0-upload-profile {} {} {} --switch".format(UPLOAD_FOLDER+file_name, nightscout, token)
				subprocess.call(command4, shell=True)
				return profile, 200
			except Exception as e:
				print(e)
				return e, 500 # RETURN STATUS CODE 500 "internal server error"

		# IF NOT VALID API REQUEST RETURN STATUS CODE 400 "Bad Request"
		else:
			return "please used right syntax",400


api.add_resource(API_class, "/api/<string:step>")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)