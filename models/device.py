from odoo import api, fields, models, _
from datetime import datetime
class Device(models.Model):
    _name= 'giot.device'

    name = fields.Char(string='Device Name', required=True)
    mac = fields.Char(string='Device MAC Address', required=True)
    dkey = fields.Char(string='Device Key', required=True)
    logs = fields.One2many('giot.device.log', 'device_id', string='Logs')
    cmds = fields.One2many('giot.device.cmd', 'device_id', string='Commands')
    is_active = fields.Boolean(string='Active', default=True)

class DeviceLog(models.Model):
    _name = 'giot.device.log'

    device_id = fields.Many2one('giot.device', string='Device', required=True)
    raw_log = fields.Text(string='Raw JSON Log')
    
    @api.model
    def append_log(self,device_mac, logs):
        # get device id
        device = self.env['giot.device'].search([('mac','=',str(device_mac))])
        if not device:
            return False
        #check each param
        self.create({
            'device_id':device.id,
            'raw_log' : logs
        })
        return True

class DeviceCmd(models.Model):
    _name = 'giot.device.cmd'
    device_id = fields.Many2one('giot.device', string='Device', required=True)
    method = fields.Selection([('ping', 'ping'),('reset','reset'),('set','set')], string='Method', required=True)
    params = fields.Char(string='Params')
    is_return  = fields.Boolean(string='Return Status', default=False, readonly=True)
    is_success = fields.Boolean(string='Success Status', default=False, readonly=True)
    
    return_data = fields.Text(string='Return Data', readonly=True)
    return_time = fields.Datetime(string='Return Time', readonly=True)

    @api.model
    def rtr_cmd(self, cmd_id, rtr_data):
        cmd = self.browse(cmd_id)
        cmd.return_data = rtr_data
        cmd.is_success = True
        cmd.return_time = datetime.now()
        
        return True
