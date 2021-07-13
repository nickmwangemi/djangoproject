from rest_framework import serializers
from typing import List, Dict, Callable, Tuple

from rest_framework.fields import empty
SlotValidationResult = Tuple[bool, bool, str, Dict]


class valueFormSerializer(serializers.Serializer):
    entity_type = serializers.CharField(required=True)
    value = serializers.CharField(required=True)

class finiteSerializer(serializers.Serializer):
                                
    invalid_trigger = serializers.CharField(required=True)
    key = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    reuse = serializers.BooleanField(required=True)
    support_multiple = serializers.BooleanField(required=True) 
    pick_first = serializers.BooleanField(required=True)
    supported_values = serializers.ListField(required=True)
    type = serializers.ListField(required=True)
    validation_parser = serializers.CharField()
    values = serializers.ListField(child = valueFormSerializer())           

    
    def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None, invalid_trigger: str = None, key: str = None,
    support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:

        # logic for when no data in value
        if len(values)==0:
            filled = False
            partially_filled = False

        # logic for validating an entity on the basis of its value extracted.
    
        extra = key
        par = list()
        for elem in values:
            for i in supported_values:
                if i in elem.values() and i not in par:
                    par.append(i) 

        # logic for pick_first
        if pick_first == True:
            params = par[0]
        else:
            params = par
    
        # logic for support_multiple
        if support_multiple == True:
            key = params
        else:
            key = '' # assumption here is that the 'ids_stated' is a list of supported IDs passed in the 'values' list. It is stored in the key variable.

        # logic for filled output
        a_key = "value"
        value_of_key = [a_dict[a_key] for a_dict in values]
        for j in value_of_key:
            if j in params:
                filled = True
            else:
                filled = False
                break
    
        # logic for partially filled
        for j in value_of_key:
            if filled == True:
                partially_filled = False
                break
            else:
                if j in par:
                    partially_filled = True
                    break
                else:
                    partially_filled = False

        # logic for trigger:
        if filled == True:
            trigger = ""
        else:
            trigger = 'invalid_ids_stated'

        # logic for parameters
        if len(par)!=0:
            parameters = {}
            parameters[extra] = par
        else:
            parameters = {}
    
        return SlotValidationResult (filled,partially_filled,trigger,parameters)






