#include "imp.hh"
#include "str.hh"
#include <vector>

std::string LastErrMsg = "GOOD";
const std::string &LastError() { return LastErrMsg; }

unsigned ErrVal() { return -1; }

static unsigned CAP = 10;
static unsigned IDX = 0;
static unsigned SIZE = 0;

static str *LPSTR = 0;
#define LPSTRIDX(i) ((IDX + (i)) % CAP)
#define LSTR(i) LPSTR[LPSTRIDX(i)]

unsigned GetCap() { return CAP; }
void SetCap(unsigned sz) {
  str *d = new str[sz]();
  if (!d) {
    LastErrMsg = "[LPSTRRESIZE] Resizing has failed.";
    return;
  }

  SIZE = sz < SIZE ? sz : SIZE;

  for (unsigned i = 0; i < SIZE; i++) {
    d[i].swap(LPSTR[(IDX + i % CAP)]);
  }

  IDX = 0;
  CAP = sz;

  if (LPSTR)
    delete LPSTR;
  LPSTR = d;
}
unsigned Size() { return SIZE; }
unsigned Append(const char *str) {
  if (SIZE == CAP) {
    LastErrMsg = "[Append] List is full.";
    return -1;
  }

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[Append] LPSTR is null.";
    return -1;
  }

  LSTR(SIZE).a[0] = str;
  SIZE++;

  return SIZE - 1;
}

unsigned Remove(unsigned begin, unsigned end) {
  if (begin > end)
    return 0;

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[Remove] LPSTR is null.";
    return -1;
  }

  for (unsigned i = 0; i < SIZE - end; i++) {
    const unsigned ii = i + CAP;

    /*
     * end - 1 == EIDX
     * begin == BIDX
     * DELIVERY COUNT: CAP - EIDX - 1 -> CAP - end
     * FEE: (EIDX - BIDX) + 1 -> end - BIDX
     * [1][0][0][1][1]
     */
    LSTR(ii).swap(LSTR(ii - (end - begin)));
  }

  SIZE = end - begin;
  return SIZE - end;
}
unsigned Swap(unsigned a, unsigned b) {
  if (a >= SIZE) {
    LastErrMsg = "[Swap] `a` is too big.";
    return -1;
  }

  if (b >= SIZE) {
    LastErrMsg = "[Swap] `b` is too big.";
    return -1;
  }

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[Swap] LPSTR is null.";
    return -1;
  }

  LSTR(a).swap(LSTR(b));
  return 0;
}
unsigned Set(unsigned i, const char *str) {
  if (i >= SIZE) {
    LastErrMsg = "[Set] `i` is too big.";
    return -1;
  }

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[Set] LPSTR is null.";
    return -1;
  }

  *LSTR(i).a = str;

  return i;
}

const std::string Get(unsigned i) {
  if (i >= SIZE) {
    LastErrMsg = "[Get] `i` is too big.";
    return "";
  }

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[Get] LPSTR is null.";
    return "";
  }

  return *LSTR(i).a;
}

void Pop() {
  IDX++;
  if (CAP == IDX) {
    IDX = 0;
  }
}

const std::vector<std::string> &GetAll() {
  static std::vector<std::string> D{};

  if (!LPSTR) {
    SIZE = CAP = IDX = 0;
    LastErrMsg = "[GetAll] LPSTR is null.";
    D = {};
    return D;
  }

  if (SIZE > D.size())
    D.resize(SIZE);

  for (unsigned i = 0; i < SIZE; i++) {
  }

  return D;
}
