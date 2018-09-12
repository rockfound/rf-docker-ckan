import ckan.plugins as p


class RFController(p.toolkit.BaseController):

    def rf(self, uri):
        data_dict = {'uri': uri}
        action = p.toolkit.get_action('ckanext-rf_rf')
        result = action({}, data_dict)
        return result
