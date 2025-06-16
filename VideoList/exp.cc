#include "./imp.hh"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(VideoList, m) {
  m.doc() = "Video List";
  m.def("LastError", &LastError, "Last Error as string");
  m.def("ErrVal", &ErrVal, "Error value. Returns unsigned -1.");
  m.def("Capacity", &GetCap, "Get current capacity.");
  m.def("SetCapacity", &SetCap, "Set current capacity.");
  m.def("Append", &Append, "Append a string");
  m.def("Remove", &Remove, "Remove from first index to last index.");
  m.def("Swap", &Swap, "Swap the values of two.");
  m.def("Set", &Set, "Set the values of index.");
  m.def("Get", &Get, "Get one value");
  m.def("GetAll", &GetAll, "Get all values");
  m.def("Pop", &Pop, "Remove the first one.");
}
