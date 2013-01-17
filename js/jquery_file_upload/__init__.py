from fanstatic import Library, Resource
import js.jquery_iframe_transport

library = Library('jquery_file_upload', 'resources')

jquery_file_upload = Resource(library,
                              'jquery.fileupload.js',
                              depends=[js.jquery_iframe_transport.jquery_iframe_transport, ])
