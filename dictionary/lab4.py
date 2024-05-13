d1 = {
    "hardware": {
        "last-change": "",
        "component": [
            {
                "name": "",
                "class": "",
                "physical-index": "",
                "description": "",
                "parent": "",
                "parent-rel-pos": "",
                "contains-child": [
                    ""
                ],
                "hardware-rev": "",
                "firmware-rev": "",
                "software-rev": "",
                "serial-num": "",
                "mfg-name": "",
                "model-name": "",
                "alias": "",
                "asset-id": "",
                "is-fru": "",
                "mfg-date": "",
                "uri": [
                    ""
                ],
                "uuid": "",
                "state": {
                    "state-last-changed": "",
                    "admin-state": "",
                    "oper-state": "",
                    "usage-state": "",
                    "alarm-state": "",
                    "standby-state": "",
                    "power-state": "ON",
                    "availability-state": ""
                },
                "sensor-data": {
                    "value": "",
                    "value-type": "",
                    "value-scale": "",
                    "value-precision": "",
                    "oper-status": "",
                    "units-display": "",
                    "value-timestamp": "",
                    "value-update-rate": ""
                },
                "label-content": {
                    "model-name": "",
                    "serial-number": ""
                },
                "product-code": "",
                "energy-saving-enabled": "True",
                "dying-gasp-support": "",
                "last-service-date": "",
                "o-ran-name": "",
                "connector-label": ""
            }
        ]
    }
}

# print(d1["hardware"]["component"][0]["state"]["power-state"])
for k, v in d1.items():
    # print(k)
    # print(type(d1[k]))
    # print(d1[k])
    # print(v)
    # print(type(v))
    if v != "" and isinstance(v, dict):
        for k1, v1 in v.items():
            # print(k1)
            if v1 != "" and isinstance(v1, list):
                # print("hello")
                # print(v1)
                for l1 in v1:
                    # print(l1)
                    # print(type(l1))
                    for k2, v2 in l1.items():
                        if v2 != "" and isinstance(v2, dict):
                            # if v2 != "":
                            #     print(k2, v2)
                            for k3, v3 in v2.items():
                                if v3 != "":
                                    print(k3, v3)
