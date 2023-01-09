from odoo import api, fields, models, _

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

    date = fields.Datetime(string='Date')

class DeviceCmd(models.Model):
    _name = 'giot.device.cmd'
    device_id = fields.Many2one('giot.device', string='Device', required=True)

    method = fields.Selection([('reset','reset'),('set','set')], string='Method', required=True)
    params = fields.Char(string='Params')

    is_executed = fields.Boolean(string='Execution Status', default=False)
    is_suceess = fields.Boolean(string='Success Status')
    is_return  = fields.Boolean(string='Return Status', default=False)

    return_data = fields.Text(string='Return Data')
