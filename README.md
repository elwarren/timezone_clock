# timezone_clock

A simple timezone clock for iOS using [Pythonista](http://omz-software.com/pythonista/) using the [scene module](http://omz-software.com/pythonista/docs/ios/scene.html).

The scene module can update 60 times per second.  Set `frame_interval=60` to refresh once per second or `frame_interval=1` to refresh as fast as possible.  This code defaults to `frame_interval=30` or twice a second.

Example output:

```
17:45:21.296 Amsterdam
16:45:21.296 UTC
11:45:21.296 New York
10:45:21.296 Chicago
09:45:21.296 Denver
08:45:21.296 San Francisco
```	

## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
