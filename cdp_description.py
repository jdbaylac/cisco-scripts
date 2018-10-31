import re
import sys
from cisco import cli 
import json
cdp_dict = {}
raw_input = clid("show cdp neighbors")

cdp_json = json.loads(raw_input)

cdp = cdp_json["TABLE_cdp_neighbor_brief_info"]["ROW_cdp_neighbor_brief_info"]
for entry in cdp:
    intf_id = entry['intf_id']
    if intf_id not in cdp_dict:
        cdp_dict[intf_id] = {}	
    cdp_dict[intf_id]['intf_id'] = intf_id
    cdp_dict[intf_id]['device_id'] = entry['device_id']
    cdp_dict[intf_id]['port_id'] = entry['port_id']
	
for key, value in cdp_dict.items():
    if 'port_id' in value and 'device_id' in value and 'intf_id' in value:
        cli('conf t ; interface ' + value['intf_id'] + ' ; description ' + value['device_id'] + ' ' + value['port_id'])	

