from flask import jsonify, make_response, Blueprint


bp = Blueprint('api', __name__, url_prefix='/api/v1')





def validate_party(item, arr, name):
	"""party validator function"""
	for key, value in item.items():
		if not value:
			return response(
				"Please provide a {} for the party".format(key), 404) #key not found
		if key == "name":
			if len(value) <3:
				return response(
					"The party name provided is too short", 416)#requested range not satisfiable
		for i in range(len(arr)):
			if arr[i]['id'] == id:
				return response("{} already exist".format(name), 406)


def generate_id(list):
	"""create a unique id for a new item appended to the list"""
	return len(list)+ 1

def response(message,code,data=None): #returns response for every method
	'''create response'''
	response = {
		'status': code,
		'message': message,
		'data':data
	}
	return make_response(jsonify(response), code)