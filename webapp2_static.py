import os
import os.path
import mimetypes
import webapp2
import logging


class StaticFileHandler(webapp2.RequestHandler):
    """A request handler for returning static files."""  
    def get(self, asset_name):
        """Serve out the contents of a file to self.response.
        Args:
        asset_name: The name of the static asset to serve. Must be in ASSETS_PATH.
        """
        abs_path = os.path.abspath(os.path.join(self.app.config.get('webapp2_static.static_file_path', 'static'), asset_name))
        try:
            with open(abs_path, 'rb') as f:
                data = f.read()
        except (OSError, IOError):
            logging.exception('Error reading file %s', abs_path)
            self.response.set_status(404)
        else:
            content_type, _ = mimetypes.guess_type(abs_path)

            assert content_type, ('cannot determine content-type for %r' % abs_path)
            self.response.headers['Content-Type'] = content_type
            self.response.out.write(data)

