from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group
import js.jquery_iframe_transport
# import js.jqueryui

library = Library('jquery_file_upload', 'resources')

# TODO replace with js.jqueryui.ui_widget once it packages something >= 1.9
res_jquery_ui_widget = Resource(library,
                                'jquery.ui.widget.js',
                                depends=[js.jquery.jquery, ])
res_upload = Resource(library,
                      'jquery.fileupload.js',
                      depends=[js.jquery_iframe_transport.jquery_iframe_transport,
                               js.jquery.jquery, ])
res_upload_ui = Resource(library,
                         'jquery.fileupload-ui.js',
                         depends=[res_upload,
                                  res_jquery_ui_widget, ])
resources = Group([res_upload, res_upload_ui, ])
