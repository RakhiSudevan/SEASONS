from osv import osv
from osv import fields

class hr_contract(osv.osv):
   
    _inherit="hr.contract"
    
 
    _columns = {
            'transport_alwnce':fields.char('Transportation Allowance', size=64, required=False, readonly=False),
            'other_alwnce':fields.char('Other Allowance', size=64, required=False, readonly=False),
            'Mobile_alwnce':fields.char('Mobile Allowance', size=64, required=False, readonly=False),
            'Petrol_alwnce':fields.char('Petrol Allowance', size=64, required=False, readonly=False),
            'House_rent_alwnce':fields.char('House Rent Allowance', size=64, required=False, readonly=False),
            'allowance':fields.char('Allowance', size=64, required=False, readonly=False),
            'air_ticket':fields.char('Air Ticket', size=64, required=False, readonly=False)
           
            
        }
hr_contract()
