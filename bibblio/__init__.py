
# coding:utf-8

import authorization
import discovery
import enrichment

client_id = ''
client_secret = ''
access_token = ''


class Token:

	@classmethod
	def get_access_token(self):
		return authorization.get_access_token(client_id, client_secret)


class Enrichment:

	@classmethod
	def create_content_item(self, payload):
		return enrichment.create_content_item(access_token, payload)

	@classmethod
	def get_content_items(self, limit=None, page=None):
		return enrichment.get_content_items(access_token, limit, page)

	@classmethod
	def get_content_item(self, content_item_id):
		return enrichment.get_content_item(access_token, content_item_id)

	@classmethod
	def update_content_item(self, content_item_id, payload):
		return enrichment.update_content_item(
			access_token,
			content_item_id,
			payload
		)

	@classmethod
	def delete_content_item(self, content_item_id):
		return enrichment.delete_content_item(access_token, content_item_id)

	@classmethod
	def metadata(self, text):
		return enrichment.metadata(access_token, text)


class Discovery:

	@classmethod
	def recommendations(self, content_item_id):
		return discovery.recommendations(access_token, content_item_id)
