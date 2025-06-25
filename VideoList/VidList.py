from .build import VList

sz_t    = int
idx_t   = int
err_t   = int

# Error msg
def LastError() -> str:
    return VList.LastError()

# Always returns error value.
def ErrVal() -> err_t:
    return VList.ErrVal()

# Get the capacity of the list.
def GetCapacity() -> sz_t:
    return VList.GetCap()

def SetCapacity(cap: int) -> sz_t:
    return VList.SetCap(cap)

def Append(a : str) -> sz_t:
    return VList.Append(a) 

def Remove(index_begin: idx_t, index_end: idx_t) -> sz_t | err_t:
    return VList.Remove(index_begin, index_end)

def Swap(a: int, b: int) -> int:
    return VList.Swap(a, b)

def Set(obj: int, a: str) -> int:
    return VList.Set(obj, a)

# kills the first element
def Pop() -> int:
    return VList.Pop()

def Get(obj: int) -> str:
    return VList.Get(obj)

def GetAll() -> list[str]:
    return VList.GetAll()
