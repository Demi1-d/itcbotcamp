a=['Alibek\n','Guluzim\n','Adi\n','Miras\n','Darhan\n']
with open('itcbootcamp', 'w') as f:
    f.writelines(a)
    f.write('Hello itc-bootcamp')