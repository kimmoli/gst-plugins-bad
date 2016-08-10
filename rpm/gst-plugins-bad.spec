%define majorminor   1.0
%define gstreamer    gstreamer

# Conditional building of X11 related things
%bcond_with X11

Summary:     GStreamer streaming media framework "bad" plug-ins
Name:        %{gstreamer}%{majorminor}-plugins-bad
Version:     1.8.2
Release:     1
License:     LGPLv2+
Group:       Applications/Multimedia
URL:         http://gstreamer.freedesktop.org/
Source:      http://gstreamer.freedesktop.org/src/gst-plugins-bad/gstreamer1.0-plugins-bad-%{version}.tar.xz
Patch1:      0001-Set-video-branch-to-NULL-after-finishing-video-recor.patch
Patch2:      0002-Keep-video-branch-in-NULL-state.patch
Patch3:      0003-photography-add-missing-vmethods.patch
Patch4:      0004-camerabin-install-GST_PHOTOGRAPHY_PROP_EXPOSURE_MODE.patch
Patch5:      0005-Downgrade-mpeg4videoparse-to-prevent-it-from-being-p.patch
Requires:      orc >= 0.4.18
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: check
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(opus)
BuildRequires: python
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

%package devel
Summary: Development files for the GStreamer media framework "bad" plug-ins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gstreamer1.0-plugins-base-devel

%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
are not tested well enough, or the code is not of good enough quality.

%prep
%setup -q -n gstreamer1.0-plugins-bad-%{version}/gst-plugins-bad
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --with-package-name='SailfishOS GStreamer Bad Plug-ins' \
  --with-package-origin='http://jolla.com' \
  --enable-debug \
  --disable-static \
  --enable-shared \
  --disable-gtk-doc \
  --disable-examples \
  --enable-gtk-doc-html=no \
  --enable-gtk-doc-pdf=no \
  --disable-nls \
  --enable-orc \
  --enable-gles2 \
%if %{with X11}
  --enable-x11=yes \
%else
  --enable-x11=no \
%endif
  --disable-adpcmdec --disable-adpcmenc --disable-asfmux \
  --disable-audiovisualizers --disable-bayer \
  --disable-cdxaparse --disable-coloreffects --disable-dataurisrc \
  --disable-dccp --disable-debugutils --disable-dvbsuboverlay \
  --disable-dvdspu --disable-faceoverlay --disable-festival --disable-fieldanalysis \
  --disable-freeverb --disable-frei0r --disable-gaudieffects \
  --disable-geometrictransform --disable-hdvparse --disable-inter --disable-interlace \
  --disable-ivfparse --disable-jp2kdecimator --disable-librfb \
  --disable-liveadder --disable-mpegdemux --disable-mpegtsmux \
  --disable-mpegpsmux --disable-mve --disable-mxf \
  --disable-nuvdemux --disable-patchdetect --disable-pcapparse \
  --disable-pnm --disable-real --disable-removesilence --disable-sdi \
  --disable-sdp --disable-segmentclip --disable-siren --disable-smooth \
  --disable-speed --disable-subenc --disable-stereo --disable-tta \
  --disable-videofilters --disable-videomeasure --disable-videosignal \
  --disable-vmnc --disable-y4m --disable-fbdev --disable-vcd \
  --disable-id3tag --disable-linsys --disable-gsettings --disable-dvb \
  --disable-decklink --disable-accurip --disable-audiofxbad --disable-ivtc \
  --disable-midi --disable-yadif --disable-mpegtsmux \
  --disable-accurip --disable-autoconvert --disable-gdp

make %{?jobs:-j%jobs}

%install
%make_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -fr $RPM_BUILD_ROOT%{_datadir}/gtk-doc

# remove waylandsink. It does not run because we do not support all the interfaces it needs.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libgstwayland-%{majorminor}.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstfragmented.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstbadbase-%{majorminor}.so.*
%{_libdir}/libgstbadvideo-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstbadbase-%{majorminor}.so
%{_libdir}/libgstbadvideo-%{majorminor}.so
%{_libdir}/libgstgl-%{majorminor}.so
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers
%{_includedir}/gstreamer-%{majorminor}/gst/insertbin
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstbasecamerasrc.h
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabin-enum.h
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc/gstcamerabinpreview.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-atsc-section.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-dvb-descriptor.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-dvb-section.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegtsdescriptor.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegtssection.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/mpegts.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gstmpegts-enumtypes.h
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts/gst-scte-section.h
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gstfragment.h
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader.h
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader_debug.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/gsteglimagememory.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/egl/gstgldisplay_egl.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gl.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/all_functions.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/base.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/blending.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/eglimage.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/fbo.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/fixedfunction.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/gles.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/gstgl_compat.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/gstgl_gles2compat.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/opengl.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/glprototypes/shaders.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgl_fwd.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglapi.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglbufferpool.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglcolorconvert.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglconfig.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglcontext.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgldisplay.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgldownload.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglfeature.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglfilter.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglframebuffer.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglmemory.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglshader.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglshadervariables.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglupload.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstgluploadmeta.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglutils.h
%{_includedir}/gstreamer-%{majorminor}/gst/gl/gstglwindow.h
%if %{with X11}
%{_includedir}/gstreamer-%{majorminor}/gst/gl/x11/gstgldisplay_x11.h
%endif
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{majorminor}.pc