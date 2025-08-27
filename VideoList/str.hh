#ifndef str_hh
#define str_hh

#include <cstdlib>
#include <string>

extern std::string LastErrMsg;

struct str {
	char* a;

	inline str(const char *a = "") {
		this->a = (char*)calloc(strlen(a) + 1, 1);


		if (!this->a) {
			LastErrMsg = "[str::str] String Allocation has failed.";
		}
	}

	inline void swap(str &_a) {
		char *tmp = a;
		this->a = _a.a;
		_a.a = tmp;
	}

	inline void setstr(const char* a) {
		char* re = (char*)realloc(this->a, strlen(a) + 1);
		if(!re) {
			LastErrMsg = "Allocation has failed.";
			return;
		}

		if(re != this->a) { free(this->a); }

		strcpy(re, a);
		this->a = re;
	}

	inline str(const str &&_a) : str(_a.a) {}

	inline ~str() {
		if (a) free(a);
		this->a = 0;
	}
};

#endif
