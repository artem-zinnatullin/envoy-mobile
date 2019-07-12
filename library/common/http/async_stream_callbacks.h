#pragma once

#include "library/common/types.h"
#include "library/common/http/utility.h"

#include "envoy/buffer/buffer.h"
#include "envoy/http/async_client.h"
#include "envoy/http/header_map.h"

namespace Envoy {
namespace Http {

class MobileAsyncStreamCallbacks : public AsyncClient::StreamCallbacks {
public:
  MobileAsyncStreamCallbacks(envoy_observer observer);
  void onHeaders(HeaderMapPtr&& headers, bool end_stream);
  void onData(Buffer::Instance& data, bool end_stream);
  void onTrailers(HeaderMapPtr&& trailers);
  void onReset();

private:
  envoy_observer observer_;
};

} // namespace Http
} // namespace Envoy
