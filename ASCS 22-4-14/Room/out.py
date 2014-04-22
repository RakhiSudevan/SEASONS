from osv import osv
from osv import fields

class ascs_out(osv.osv):
 
    _name = 'ascs.out'
    _description = 'ascs.out'
 
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
ascs_out()