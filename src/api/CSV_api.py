from FlexStrat.API import api

@api
class CSV_file:
    def run(self,*args,**kwargs):
        print(args)
        print(kwargs)