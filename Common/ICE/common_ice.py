# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.7.1
#
# <auto-generated>
#
# Generated from file `common.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module common
_M_common = Ice.openModule('common')
__name__ = 'common'

if '_t_byteArray' not in _M_common.__dict__:
    _M_common._t_byteArray = IcePy.defineSequence('::common::byteArray', (), IcePy._t_byte)

_M_common._t_CommonService = IcePy.defineValue('::common::CommonService', Ice.Value, -1, (), False, True, None, ())

if 'CommonServicePrx' not in _M_common.__dict__:
    _M_common.CommonServicePrx = Ice.createTempClass()
    class CommonServicePrx(Ice.ObjectPrx):

        def request(self, flag, params, context=None):
            return _M_common.CommonService._op_request.invoke(self, ((flag, params), context))

        def requestAsync(self, flag, params, context=None):
            return _M_common.CommonService._op_request.invokeAsync(self, ((flag, params), context))

        def begin_request(self, flag, params, _response=None, _ex=None, _sent=None, context=None):
            return _M_common.CommonService._op_request.begin(self, ((flag, params), _response, _ex, _sent, context))

        def end_request(self, _r):
            return _M_common.CommonService._op_request.end(self, _r)

        def requestWithByteIn(self, flag, params, requestData, context=None):
            return _M_common.CommonService._op_requestWithByteIn.invoke(self, ((flag, params, requestData), context))

        def requestWithByteInAsync(self, flag, params, requestData, context=None):
            return _M_common.CommonService._op_requestWithByteIn.invokeAsync(self, ((flag, params, requestData), context))

        def begin_requestWithByteIn(self, flag, params, requestData, _response=None, _ex=None, _sent=None, context=None):
            return _M_common.CommonService._op_requestWithByteIn.begin(self, ((flag, params, requestData), _response, _ex, _sent, context))

        def end_requestWithByteIn(self, _r):
            return _M_common.CommonService._op_requestWithByteIn.end(self, _r)

        def requestWithByteOut(self, flag, params, context=None):
            return _M_common.CommonService._op_requestWithByteOut.invoke(self, ((flag, params), context))

        def requestWithByteOutAsync(self, flag, params, context=None):
            return _M_common.CommonService._op_requestWithByteOut.invokeAsync(self, ((flag, params), context))

        def begin_requestWithByteOut(self, flag, params, _response=None, _ex=None, _sent=None, context=None):
            return _M_common.CommonService._op_requestWithByteOut.begin(self, ((flag, params), _response, _ex, _sent, context))

        def end_requestWithByteOut(self, _r):
            return _M_common.CommonService._op_requestWithByteOut.end(self, _r)

        def requestWithByteInOut(self, flag, params, requestData, context=None):
            return _M_common.CommonService._op_requestWithByteInOut.invoke(self, ((flag, params, requestData), context))

        def requestWithByteInOutAsync(self, flag, params, requestData, context=None):
            return _M_common.CommonService._op_requestWithByteInOut.invokeAsync(self, ((flag, params, requestData), context))

        def begin_requestWithByteInOut(self, flag, params, requestData, _response=None, _ex=None, _sent=None, context=None):
            return _M_common.CommonService._op_requestWithByteInOut.begin(self, ((flag, params, requestData), _response, _ex, _sent, context))

        def end_requestWithByteInOut(self, _r):
            return _M_common.CommonService._op_requestWithByteInOut.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_common.CommonServicePrx.ice_checkedCast(proxy, '::common::CommonService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_common.CommonServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::common::CommonService'
    _M_common._t_CommonServicePrx = IcePy.defineProxy('::common::CommonService', CommonServicePrx)

    _M_common.CommonServicePrx = CommonServicePrx
    del CommonServicePrx

    _M_common.CommonService = Ice.createTempClass()
    class CommonService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::common::CommonService')

        def ice_id(self, current=None):
            return '::common::CommonService'

        @staticmethod
        def ice_staticId():
            return '::common::CommonService'

        def request(self, flag, params, current=None):
            raise NotImplementedError("servant method 'request' not implemented")

        def requestWithByteIn(self, flag, params, requestData, current=None):
            raise NotImplementedError("servant method 'requestWithByteIn' not implemented")

        def requestWithByteOut(self, flag, params, current=None):
            raise NotImplementedError("servant method 'requestWithByteOut' not implemented")

        def requestWithByteInOut(self, flag, params, requestData, current=None):
            raise NotImplementedError("servant method 'requestWithByteInOut' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_common._t_CommonServiceDisp)

        __repr__ = __str__

    _M_common._t_CommonServiceDisp = IcePy.defineClass('::common::CommonService', CommonService, (), None, ())
    CommonService._ice_type = _M_common._t_CommonServiceDisp

    CommonService._op_request = IcePy.Operation('request', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (), ((), IcePy._t_string, False, 0), ())
    CommonService._op_requestWithByteIn = IcePy.Operation('requestWithByteIn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), _M_common._t_byteArray, False, 0)), (), ((), IcePy._t_string, False, 0), ())
    CommonService._op_requestWithByteOut = IcePy.Operation('requestWithByteOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0)), (((), _M_common._t_byteArray, False, 0),), ((), IcePy._t_string, False, 0), ())
    CommonService._op_requestWithByteInOut = IcePy.Operation('requestWithByteInOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), _M_common._t_byteArray, False, 0)), (((), _M_common._t_byteArray, False, 0),), ((), IcePy._t_string, False, 0), ())

    _M_common.CommonService = CommonService
    del CommonService

# End of module common