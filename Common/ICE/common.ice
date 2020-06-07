module common
{
    sequence<byte> byteArray;

   interface CommonService
   {
        string request(int flag, string params);
        string requestWithByteIn(int flag, string params, byteArray requestData);
        string requestWithByteOut(int flag, string params, out byteArray responseData);
        string requestWithByteInOut(int flag, string params, byteArray requestData, out byteArray responseData);
   };
};
