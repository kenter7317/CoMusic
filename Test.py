from VideoList import VidList

print(dir(VidList))
print(VidList.LastError())

# this is an error value.
print(VidList.ErrVal())
print(VidList.GetCapacity())
print(VidList.SetCapacity(14))
print(f"GetCapacity: {VidList.GetCapacity()}")

print(VidList.Append("Hello World!"))
print(VidList.Append("Hello World! 2"))
print(VidList.GetAll())

print(VidList.Remove(0, 5))
print(VidList.LastError())

print(VidList.Remove(0, 2))
print(VidList.GetAll())

print(VidList.Append("Hello World!"))
print(VidList.Append("Hello World! 2"))
print(VidList.GetAll())
print(VidList.Swap(0, 1))
print(VidList.GetAll())


print(VidList.Swap(0, 5))
print(VidList.LastError())


print(VidList.Get(1))
print(VidList.Set(0, "Nothing"))
print(VidList.Get(0))
print(VidList.GetAll())

print(VidList.Pop())
print(VidList.GetAll())

print(VidList.Pop())
print(VidList.GetAll())

# if it gets an error, this is expected.
print(VidList.Pop())
print(VidList.GetAll())
print(VidList.LastError())
