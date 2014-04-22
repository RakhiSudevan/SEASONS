from osv import osv
from osv import fields

class ascs_innn(osv.osv):
 
    _name = 'ascs.innn'
    _description = 'ascs.innn'
 
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
ascs_innn()