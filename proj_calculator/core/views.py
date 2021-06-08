from django.shortcuts import render

def home_page(request):
    ans = None
    if request.method == 'POST':
        print(request.POST)
        inp_str = request.POST['input_str']
        print(inp_str)
        operaters = ["+", "-", "*", "/"]
        # [1] check validation
        if any(operater in inp_str for operater in operaters):
            print("yes") # solve the input
            #[2] check wheather to use BODMAS or Not
            count = 0
            for operater in operaters:
                count += inp_str.count(operater)
            # print(count)
            if count==1:
                # simple
                if "+" in inp_str:
                    ans = int(inp_str.split("+")[0]) + int(inp_str.split("+")[1])
                elif "-" in inp_str:
                    ans = int(inp_str.split("-")[0]) - int(inp_str.split("-")[1])
                elif "*" in inp_str:
                    ans = int(inp_str.split("*")[0]) * int(inp_str.split("*")[1])
                elif "/" in inp_str:
                    ans = int(inp_str.split("/")[0]) - int(inp_str.split("/")[1])
            else:
                # BODMAS
                pass
            
            print(ans)

        else:
            print("No") # send Syntax Error to cal


    return render(request, 'home.html',context={"ans": ans})