import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

def link(resource_id):
    return '%s%s' % (action.base_url(), resource_id)

class RFPlugin(p.SingletonPlugin):

    p.implements(p.IConfigurer)

    def update_config(self, config):
        import logging
        logging.warning('RF Plugin update_config is running! ... adding directory templates and public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
