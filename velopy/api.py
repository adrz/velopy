import mimetypes
import httplib
from socket import timeout
from threading import Thread
from time import sleep
import json

class api(object):
	def __init__(self, api_key=None):

		self.host 	= 'api.jcdecaux.com'
		self.api_key 	= api_key
		self.headers    = 'HTTP/1.1'
		self.version 	= '/vls/v1/'
		self.conn 	= httplib.HTTPSConnection(self.host)
		

	def getContracts(self):
		url = self.version + 'contracts&apiKey=' + self.api_key
		#conn = httplib.HTTPSConnection(self.host)
		self.conn.request('GET',url,self.headers)
		resp = self.conn.getresponse()
		if resp.status != 200:
			print "ERROR !"
		else:
			return resp.read()

	def getCSVstation(self,station_number=None,contract='Paris'):
		url = self.version + 'stations/' + str(station_number) + '?contract=' + contract + '&apiKey=' + self.api_key
		#conn = httplib.HTTPSConnection(self.host)
		self.conn.request('GET',url,self.headers)
		resp = self.conn.getresponse()
		if resp.status != 200:
			print "ERROR!"
		else:
			return self._parserCSV(json.loads(resp.read()))

	def getCSVallstations(self,contract='Paris'):
		url = self.version + 'stations/?contract=' + contract + '&apiKey=' + self.api_key
		#conn = httplib.HTTPSConnection(self.host)
		self.conn.request('GET',url,self.headers)
		resp = self.conn.getresponse()
		if resp.status != 200:
			print "ERROR!"
		else:
			return self._parserCSV(json.loads(resp.read()))

	@staticmethod

	def _parserCSV(all_json_items):
		out = ''
		for json_items in all_json_items:
			out = out + str(json_items['number'])
			#out = out + ',' + json_items['name']
			#out = out + ',' + json_items['address']
			out = out + ',' + str(json_items['position']['lat'])
			out = out + ',' + str(json_items['position']['lng'])
			out = out + ',' + str(json_items['banking'])
			out = out + ',' + str(json_items['bonus'])
			out = out + ',' + json_items['status']
			out = out + ',' + str(json_items['bike_stands'])
			out = out + ',' + str(json_items['available_bike_stands'])
			out = out + ',' + str(json_items['available_bikes'])
			out = out + ',' + str(json_items['last_update'])
			out = out + '\n'
		return out.encode('utf-8')

	def _version():
		return 1.0
	
