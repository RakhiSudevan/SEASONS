from osv import osv
from osv import fields

class report_report(osv.osv):

    _name = 'report.report'
    _description = 'report.report'
 
    _columns = {
            'name':fields.char('data', size=64, required=False, readonly=False)
        }
report_report()