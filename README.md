# StackStorm Zendesk Lite Pack

Offers basic Zendesk actions.

## Configuration

Copy the example configuration in [zendesklite.config.sample]
to `/opt/stackstorm/configs/zendesklite.config.sample` and edit as required.

It must contain:

* ``token`` - Authentication Token from your Zendesk API.
* ``subdomain`` - Subdomain of your Zendesk API.

## Actions

* `create.ticket` - Creates a Zendesk ticket.
