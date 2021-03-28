


class Investor:
    def __init__(self, name: str, requested_amount: float, average_amount: float):
        self.requested_amount = requested_amount
        self.name = name
        self.average_amount = average_amount

    def get_dict(self) -> dict:
        inv_dict = {}
        inv_dict['name'] = self.name
        inv_dict['requested_amount'] = self.requested_amount
        inv_dict['average_amount'] = self.average_amount
        return inv_dict


class Proration:
    def __init__(self, investors_dic: list, allocation_amount: float):
        """
        Proration constructor
        :param investors: the dictionary of all investors information
        :param allocation_amount: the total allocation amount
        """
        self.allocation_amount = allocation_amount
        self.investors = {}
        for investor in investors_dic:
            self.investors[investor.name] = investor

    def get_list(self) -> list:
        inv_list = []
        for name in self.investors:
            inv_list.append(self.investors[name].get_dict())
        return inv_list


    def requested_sum(self) -> float:
        """

        :return: the sum of all investors requested amount
        """
        req_sum = 0
        for name in self.investors:
            req_sum += self.investors[name].requested_amount
        return req_sum

    def average_sum(self) -> float:
        """

        :return: the sum of all investors history average
        """
        ave_sum = 0
        for name in self.investors:
            ave_sum += self.investors[name].average_amount
        return ave_sum

    def real_allocation(self) -> dict:
        """
        proration allocation method
        :return: the dict of inverstors' names and real allocation amount
        """
        allocation = {}
        # if poll is larger than requested sum, everyone is happy
        if self.requested_sum() < self.allocation_amount:
            for name in self.investors:
                allocation[name] = self.investors[name].requested_amount
            return allocation

        # running the allocation method until the poll is 0
        while self.allocation_amount > 0:
            estimate = {}
            requested = {}
            # 1. the sum of the all investors' history average
            avg_sum = self.average_sum()

            # 2. record the estimation amount and requested amount
            for name in self.investors:
                if name not in allocation:
                    allocation[name] = 0
                weight = self.investors[name].average_amount / avg_sum
                estimate[name] = weight * self.allocation_amount
                requested[name] = self.investors[name].requested_amount

            # 3. compare the estimation amount and requested amount
            #    and update the investors information
            for name in estimate:
                # if not enough to allocate, only allocate requested amount
                if estimate[name] > requested[name]:
                    self.allocation_amount -= requested[name]
                    del self.investors[name]
                    allocation[name] += requested[name]
                # else allocate the estimate amount
                else:
                    self.allocation_amount -= estimate[name]
                    self.investors[name].requested_amount -= estimate[name]
                    allocation[name] += estimate[name]

        return allocation
