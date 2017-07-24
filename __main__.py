import requests


def main(args):
	query_string = args.get('__ow_query',None)
	if query_string:
		parameters = {query_string[0] : query_string[1] for query_string in [query_string.split("=") for query_string in query_string.split("&") ]}
		if "domain" in parameters:
			domain = parameters["domain"]
			try:
				rsp = requests.get(domain)
				return {"ping":"yes", "domain": str(domain)}
			except:
				return {"ping":"no", "domain": str(domain)}
	return {"error":"Error while pinging"}
