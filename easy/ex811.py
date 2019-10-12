class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dic = {}
        for cpdomain in cpdomains:
            count, domain = tuple(cpdomain.split(' '))
            count = int(count)
            domain = domain.split('.')
            for i in range(len(domain)):
                subdomain = '.'.join(domain[i:])
                if subdomain in domain_dic:
                    domain_dic[subdomain] += count
                else:
                    domain_dic[subdomain] = count
        return [str(item[1]) + ' ' +  item[0] for item in domain_dic.items()]