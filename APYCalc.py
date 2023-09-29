from tkinter import *

def clicked():
    # init answer field
    daily_ROI = Label(window, text="Daily ROI (%)")
    daily_ROI_val = Entry(window, width=35, borderwidth=5)
    dr = float(base_APY_input.get())/365
    daily_ROI_val.insert(0, str("{:.2f}".format(dr)))

    daily_token_ROI = Label(window, text="Daily Return")
    daily_token_ROI_value = Entry(window, width=35, borderwidth=5)
    dtr = float(init_inv_input.get()) * (float(daily_ROI_val.get())/100)
    daily_token_ROI_value.insert(0, str("{:.4f}".format(dtr)) + " $")

    compound_APY = Label(window, text="Compound Interest")
    compound_APY_val = Entry(window, width=35, borderwidth=5)
    sum = float(init_inv_input.get())
    for i in range(1, 365):
        sum += sum*(float(daily_ROI_val.get())/10) - float(gas_fees_input.get()) - float(gas_fees_input.get())
    capy = float(init_inv_input.get()) * (1 + float(daily_ROI_val.get())/100) ** int(compound_days_input.get())
    fin = (capy - float(init_inv_input.get())) / float(init_inv_input.get()) * 100
    compound_APY_val.insert(0, str("{:.2f}".format(fin)) + "%")
        
    final_tokens = Label(window, text="Profit after Compounding")
    final_tokens_val = Entry(window, width=35, borderwidth=5)

    comp_int = float(init_inv_input.get()) * fin/100

    #sum = float(init_inv_input.get())
    # for i in range(1, int(compound_days_input.get())):
    #     sum += sum*(float(daily_ROI_val.get())/10) - float(gas_fees_input.get())
    final_tokens_val.insert(0, str("{:.4f}".format(comp_int)) + " $")

    # build grid
    daily_ROI.grid(row=5, column=0)
    daily_ROI_val.grid(row=6, column=0)

    daily_token_ROI.grid(row=5, column=1)
    daily_token_ROI_value.grid(row=6, column=1)

    compound_APY.grid(row=7, column=0)
    compound_APY_val.grid(row=8, column=0)

    final_tokens.grid(row=7, column=1)
    final_tokens_val.grid(row=8, column=1)

def selected(event):
    if(dropD.get() == 'ATOM'):
        gas_fees_input.delete(0, 'end')
        gas_fees_input.insert(0, "0.11")
    elif(dropD.get() == 'JUNO'):
        gas_fees_input.delete(0, 'end')
        gas_fees_input.insert(0, "0.01")
    elif(dropD.get() == 'OSMO'):
        gas_fees_input.delete(0, 'end')
        gas_fees_input.insert(0, "0")
    elif(dropD.get() == 'DVPN'):
        gas_fees_input.delete(0, 'end')
        gas_fees_input.insert(0, "0")
    if(dropD.get() == 'ION'):
        gas_fees_input.delete(0, 'end')
        gas_fees_input.insert(0, "0")
        

# main
window = Tk()
window.title("APY Calculator")

# init field
init_inv = Label(window, text="Initial Investment ($)")
init_inv_input = Entry(window, width=35, borderwidth=5)

base_APY = Label(window, text="Base APR")
base_APY_input = Entry(window, width=35, borderwidth=5)

gas_fees = Label(window, text="Gas fees per Compound")
gas_fees_input = Entry(window, width=35, borderwidth=5)

compound_days = Label(window, text="Compound Days")
compound_days_input = Entry(window, width=35, borderwidth=5)

submit = Button(window, text="Calculate", command=clicked)

dropD = StringVar(window)
args = ["ATOM", "JUNO", "OSMOSIS","DVPN", "ION"]
dropD.set(args[0])

dropDMenu = OptionMenu(window, dropD, *args, command=selected)

dd = Label(window, text="Token")

# build grid
init_inv.grid(row=0, column=0)
init_inv_input.grid(row=1, column=0)

base_APY.grid(row=2, column=0)
base_APY_input.grid(row=3, column=0)

compound_days.grid(row=0, column=1)
compound_days_input.grid(row=1, column=1)

gas_fees.grid(row=2, column=1)
gas_fees_input.grid(row=3, column=1)

dd.grid(row=4, column=0)
dropDMenu.grid(row=5, column=0)

submit.grid(row=5, column=1)

window.mainloop()