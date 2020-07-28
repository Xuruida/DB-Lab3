from django.shortcuts import render

from rest_framework import views, status
from rest_framework.response import Response

from .models import BranchInfo
from account.models import LoanInfo, ReleaseInfo, AccountBase

import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.


class BranchStats(views.APIView):

    def get(self, request, format=None):
        """
        Return stats for each branch
        """
        # get all branches
        branchList = BranchInfo.objects.all()
        print(branchList)

        statList = []

        # for each branch
        for br in branchList:
            print(br.id, br.name, br.city)
            brStat = {
                'branch_id': br.id,
                'name': br.name,
                'city': br.city
            }

            # monthly stats
            now = datetime.datetime.now()
            year = now.year - 1
            month = now.month + 1
            brStat["month"] = []
            while (year < now.year or (year <= now.year and month <= now.month)):
                if (month > 12):
                    year += 1
                    month = 1
                print('%s-%s' % (year, month))

                # Loan Stat
                monthlyLoan = LoanInfo.objects.filter(
                    branch=br.id).filter(create_time__year=year).filter(create_time__month=month)
                totalLoanAmount = sum([item.total_amount for item in monthlyLoan])

                # Release Stat
                monthlyRelease = ReleaseInfo.objects.filter(
                    loan__branch = br.id).filter(time__year=year).filter(time__month=month)
                totalReleaseAmount = sum([item.amount for item in monthlyRelease])

                print(monthlyLoan, totalLoanAmount, totalReleaseAmount)
                # Account Stat

                monthlyAccountList = AccountBase.objects.filter(branch=br.id).filter(
                    open_date__year=year).filter(open_date__month=month)

                monthlySVList = []
                monthlyCKList = []

                for item in monthlyAccountList:
                    if item.is_savings:
                        monthlySVList.append(item)
                    else:
                        monthlyCKList.append(item)

                totalSVAmount = sum([item.savings.balance for item in monthlySVList])
                totalCKAmount = sum([item.checking.overdraft for item in monthlyCKList])

                print(monthlySVList, totalSVAmount, '\n', monthlyCKList, totalCKAmount)

                # Save in 'month'
                brStat["month"].append(
                    {
                        'time': '%s-%s' % (year, month),
                        'loan': [{
                            'loan_id': item.loan_ID,
                            'total_amount': item.total_amount,
                            'create_time': item.create_time
                         } for item in monthlyLoan],
                        'loan_amount': totalLoanAmount,
                        'release': [{
                            'release_id': item.id,
                            'release_amount': item.amount,
                            'release_time': item.time
                        } for item in monthlyRelease],
                        'release_amount': totalReleaseAmount,
                        'savings': map(lambda i: i.account_ID, monthlySVList),
                        'savings_amount': totalSVAmount,
                        'checking': map(lambda i: i.account_ID, monthlyCKList),
                        'checking_amount': totalCKAmount,
                    }
                )

                # next month
                month += 1

            statList.append(brStat)
        return Response(statList, status=status.HTTP_200_OK)
