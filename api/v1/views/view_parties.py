from flask import Blueprint
from flask import request
from flask import jsonify 
from flask import make_response

from start_views import validate_party, response, generate_id
from start_views import bp

parties = []

@bp.route('/parties', methods=['POST','GET']) #create a political party
def create_party():
	
	if request.method == 'POST':
		"""create party end point"""
		data = request.get_json(force = True) #parse and get data in Json
		if not data:
			return response("No data available", 404) #No data found

		try:
			name = data['name']
			hq_address = data['hq_address']
			logo_url=data['logo_url']
			slogan = data['slogan']
		except KeyError as e:
			return response("{} field is required".format(e.args[0]), 404) #key not found
		#party details
		party = {
			"id":generate_id(parties),
			"name": name,
			"hq_address": hq_address,
			"logo_url": logo_url,
			"slogan":slogan,
		}
		
		#function validating party details
		validate_party(party, parties, 'Party') 

		#append new party to list
		parties.append(party)

		#return list of parties to display added party
		return response("Party created successfully", 201,party)

	elif request.method == 'GET':
		""" Get all parties"""
 		return response('Request was sent successfully', 201, parties)



