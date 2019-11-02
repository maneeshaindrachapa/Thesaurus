
# coding: utf-8

# In[21]:


data = ''
counter = 0
for text_idx, file in enumerate(['tr.cc.si.300_4.vec','tr.cc.si.300_5.vec']):
    with open("Output/"+file, 'r',encoding="utf8") as fp:
        file_data = fp.read().split("\n",1)
        data += file_data[1]
        print("Count:",file_data[0].split()[0])
        counter += int(file_data[0].split()[0])
print("Total count:",counter)


# In[23]:


first_line = str(counter)+" 300\n"
# data.insert(0,first_line)
to_write = first_line+data
writer = open("Output/Combined/tr.cc.si.300.vec", "w", encoding="utf-8")
writer.write(to_write)
print("====> Done <====")

