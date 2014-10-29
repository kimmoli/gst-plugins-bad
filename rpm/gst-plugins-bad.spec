%define majorminor   1.0
%define gstreamer    gstreamer

Summary:     GStreamer streaming media framework "bad" plug-ins
Name:        %{gstreamer}%{majorminor}-plugins-bad
Version:     1.2.0
Release:     1
License:     LGPLv2+
Group:       Applications/Multimedia
URL:         http://gstreamer.freedesktop.org/
Source:      http://gstreamer.freedesktop.org/src/gst-plugins-bad/gstreamer1.0-plugins-bad-%{version}.tar.xz
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: check
BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(orc-0.4)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: python
BuildRequires: autoconf213
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
  --disable-adpcmdec --disable-adpcmenc --disable-aiff --disable-asfmux \
  --disable-audiovisualizers --disable-bayer \
  --disable-cdxaparse --disable-coloreffects --disable-dataurisrc \
  --disable-dccp --disable-debugutils --disable-dvbsuboverlay \
  --disable-dvdspu --disable-faceoverlay --disable-festival --disable-fieldanalysis \
  --disable-freeverb --disable-frei0r --disable-gaudieffects \
  --disable-geometrictransform --disable-hdvparse --disable-inter --disable-interlace \
  --disable-ivfparse --disable-jp2kdecimator --disable-librfb \
  --disable-liveadder --disable-mpegdemux --disable-mpegtsdemux --disable-mpegtsmux \
  --disable-mpegpsmux --disable-mve --disable-mxf \
  --disable-nuvdemux --disable-patchdetect --disable-pcapparse \
  --disable-pnm --disable-real --disable-removesilence --disable-sdi \
  --disable-sdp --disable-segmentclip --disable-siren --disable-smooth \
  --disable-speed --disable-subenc --disable-stereo --disable-tta \
  --disable-videofilters --disable-videomeasure --disable-videosignal \
  --disable-vmnc --disable-y4m --disable-fbdev --disable-vcd \
  --disable-id3tag --disable-linsys --disable-gsettings --disable-hls --disable-dvb \
  --disable-decklink --disable-accurip --disable-audiofxbad --disable-ivtc \
  --disable-midi --disable-yadif --disable-mpegtsdemux --disable-mpegtsmux \
  --disable-accurip --disable-autoconvert --disable-gdp --disable-mfc

make %{?jobs:-j%jobs}

%install
%make_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -fr $RPM_BUILD_ROOT%{_datadir}/gtk-doc


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
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
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gstfragment.h
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader.h
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader/gsturidownloader_debug.h
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
