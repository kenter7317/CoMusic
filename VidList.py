import VideoList

sz_t    = int
idx_t   = int
err_t   = int

# Error msg
def LastError() -> str:
    return VideoList.LastError()

# Always returns error value.
def ErrVal() -> err_t:
    return VideoList.ErrVal()

# Get the capacity of the list.
def GetCapacity() -> sz_t:
    return VideoList.GetCap()

def SetCapacity(cap: int) -> sz_t:
    return VideoList.SetCap(cap)

def Append(a : str) -> sz_t:
    return VideoList.Append(a) 

def Remove(index_begin: idx_t, index_end: idx_t) -> sz_t | err_t:
    return VideoList.Remove(index_begin, index_end)

def Swap(a: int, b: int) -> int:
    return VideoList.Swap(a, b)

def Set(obj: int, a: str) -> int:
    return VideoList.Set(obj, a)

# kills the first element
def Pop() -> int:
    return VideoList.Pop()

def Get(obj: int) -> str:
    return VideoList.Get(obj)

def GetAll() -> list[str]:
    return VideoList.GetAll()
