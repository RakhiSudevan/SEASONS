from osv import osv
from osv import fields

class ascs_hr(osv.osv):

    _inherit='hr.employee'
 
    _columns = {
            'employee_id':fields.char('Employee ID', size=64, required=True, readonly=False),
            'date_of_join':fields.date('Date of Join', size=64, required=False, readonly=False),
            'expiry':fields.date('Expiry', size=64, required=False, readonly=False),
            'bank_code':fields.char('Bank Routine Code', size=64, required=False, readonly=False),
            'bank_name':fields.char('Bank Name', size=64, required=False, readonly=False),
            'father_name':fields.char('Father Name', size=64, required=False, readonly=False),
            'mother_name':fields.char('Mother Name', size=64, required=False, readonly=False),
            'pp_expiry':fields.date('Passport Expiry', size=64, required=False, readonly=False),
            'labour_expiry':fields.date('Labour Card Expiry', size=64, required=False, readonly=False),
            'cina_expiry':fields.date('Cina Expiry', size=64, required=False, readonly=False),
            'emirates_expiry':fields.date('Emirates ID Expiry', size=64, required=False, readonly=False),
            'damam_expiry':fields.date('Damam Expiry', size=64, required=False, readonly=False), 
            'marital_status': fields.selection([('single', 'Single'), ('married', 'Married')], 'Marital Status')            
            
            
            }
           
ascs_hr()