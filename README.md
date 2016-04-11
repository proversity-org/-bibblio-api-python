# Bibblio API Python
Python wrapper of Bibblio API

## Install
```pip install bibblio```

## Configuration
```import bibblio```

set client_id and client_secret

```bibblio.client_id = '1234'```

```bibblio.client_secret = '1234567890'```

get access_token

```bibblio.access_token = bibblio.Token.get_access_token()```

## Usage

For more information use [Bibblio API Documentation](http://docs.bibblio.apiary.io/)
* payload is always a dict
* limit and page are optional and integers
* text is a string
* content_item_id is a string

### Enrichment

```bibblio.Enrichment.create_content_item(payload)```

```bibblio.Enrichment.get_content_items(limit=10, page=1)```

```bibblio.Enrichment.get_content_item(content_item_id)```

```bibblio.Enrichment.update_content_item(content_item_id, payload)```

```bibblio.Enrichment.delete_content_item(content_item_id)```

```bibblio.Enrichment.metadata(text)```

### Discovery

```bibblio.Discovery.recommendations(content_item_id)```
