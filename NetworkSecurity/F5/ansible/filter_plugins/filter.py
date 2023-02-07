'''
The filter will be used for updating a pool members list of dicts
to make it more easy to consumer for ansible tasks
'''

class FilterModule:
    '''
    This class is used for the use of formatting data passed by ansible
    for the use consumption by other ansible task
    '''

    def filters(self):
        '''
        return list of  pool members settings
        '''

        return {'return_list': self.return_list}

    @staticmethod
    def return_list(var_list):
        '''
        updates pool members with a new key/pair to 
        define virtual server pool name within each node
        configuration.
        '''
        new_pool_member_list = []
        for pool in var_list:
            for member in pool["pool_members"]:
                member["pool_name"] = pool["pool_name"]            
                new_pool_member_list.append(member)


        return new_pool_member_list
