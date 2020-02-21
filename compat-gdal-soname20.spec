#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gdal-soname20
Version  : 2.2.3
Release  : 10
URL      : https://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.xz
Source0  : https://download.osgeo.org/gdal/2.2.3/gdal-2.2.3.tar.xz
Summary  : Geospatial Data Abstraction Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-2.0 Libpng MIT Qhull
Requires: compat-gdal-soname20-lib = %{version}-%{release}
Requires: compat-gdal-soname20-license = %{version}-%{release}
BuildRequires : SFCGAL-dev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : curl-dev
BuildRequires : expat-dev
BuildRequires : geos-dev
BuildRequires : giflib-dev
BuildRequires : hdf5-dev
BuildRequires : json-c
BuildRequires : json-c-dev
BuildRequires : libfastjson-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libwebp-dev
BuildRequires : libxml2-dev
BuildRequires : ocl-icd-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : postgresql-dev
BuildRequires : qhull-dev
BuildRequires : tiff-dev
BuildRequires : unixODBC-dev
BuildRequires : util-linux
BuildRequires : xerces-c-dev
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: 0001-Fix-compilation-error-on-json-c-external-link.patch
Patch2: CVE-2019-17545.patch

%description
The .i files in this directory are generated files and should not be edited
manually.

%package lib
Summary: lib components for the compat-gdal-soname20 package.
Group: Libraries
Requires: compat-gdal-soname20-license = %{version}-%{release}

%description lib
lib components for the compat-gdal-soname20 package.


%package license
Summary: license components for the compat-gdal-soname20 package.
Group: Default

%description license
license components for the compat-gdal-soname20 package.


%prep
%setup -q -n gdal-2.2.3
cd %{_builddir}/gdal-2.2.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582251784
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --datadir=/usr/share/gdal \
--with-libtiff=yes \
--with-png=yes \
--with-gif=/usr \
--with-libtool=yes \
--with-libjson-c=/usr
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1582251784
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-gdal-soname20
cp %{_builddir}/gdal-2.2.3/LICENSE.TXT %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/3c5056c99522acf3d9e2c2a2f61fdeeffced4174
cp %{_builddir}/gdal-2.2.3/alg/internal_libqhull/COPYING.txt %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/baf1d15dcf66b1e1dfee80eb405aa73105842017
cp %{_builddir}/gdal-2.2.3/frmts/gif/giflib/COPYING %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1
cp %{_builddir}/gdal-2.2.3/frmts/mrf/libLERC/LICENSE.TXT %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/3035b519169390d1aaa3a43267deaae5cdff8a9b
cp %{_builddir}/gdal-2.2.3/frmts/pcraster/libcsf/COPYING %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/1d982db70b88f943cc7d15013c28a126339d6cbc
cp %{_builddir}/gdal-2.2.3/frmts/png/libpng/LICENSE %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/1f906240d40bc72f70c6765ed4df959defd3c153
cp %{_builddir}/gdal-2.2.3/ogr/ogrsf_frmts/geojson/libjson/COPYING %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/0cd23537e3c32497c7b87157b36f9d2eb5fca64b
cp %{_builddir}/gdal-2.2.3/ogr/ogrsf_frmts/shape/COPYING %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/df97bdf33b01f9ed42a799dd3ed7a1599dd0cb9d
cp %{_builddir}/gdal-2.2.3/port/LICENCE_minizip %{buildroot}/usr/share/package-licenses/compat-gdal-soname20/f7f1d88d0aea6c567a2c351b08b0fe80f2582054
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/gdal-config
rm -f %{buildroot}/usr/bin/gdal_contour
rm -f %{buildroot}/usr/bin/gdal_grid
rm -f %{buildroot}/usr/bin/gdal_rasterize
rm -f %{buildroot}/usr/bin/gdal_translate
rm -f %{buildroot}/usr/bin/gdaladdo
rm -f %{buildroot}/usr/bin/gdalbuildvrt
rm -f %{buildroot}/usr/bin/gdaldem
rm -f %{buildroot}/usr/bin/gdalenhance
rm -f %{buildroot}/usr/bin/gdalinfo
rm -f %{buildroot}/usr/bin/gdallocationinfo
rm -f %{buildroot}/usr/bin/gdalmanage
rm -f %{buildroot}/usr/bin/gdalserver
rm -f %{buildroot}/usr/bin/gdalsrsinfo
rm -f %{buildroot}/usr/bin/gdaltindex
rm -f %{buildroot}/usr/bin/gdaltransform
rm -f %{buildroot}/usr/bin/gdalwarp
rm -f %{buildroot}/usr/bin/gnmanalyse
rm -f %{buildroot}/usr/bin/gnmmanage
rm -f %{buildroot}/usr/bin/nearblack
rm -f %{buildroot}/usr/bin/ogr2ogr
rm -f %{buildroot}/usr/bin/ogrinfo
rm -f %{buildroot}/usr/bin/ogrlineref
rm -f %{buildroot}/usr/bin/ogrtindex
rm -f %{buildroot}/usr/bin/testepsg
rm -f %{buildroot}/usr/etc/bash_completion.d/gdal-bash-completion.sh
rm -f %{buildroot}/usr/include/cpl_atomic_ops.h
rm -f %{buildroot}/usr/include/cpl_aws.h
rm -f %{buildroot}/usr/include/cpl_config.h
rm -f %{buildroot}/usr/include/cpl_config_extras.h
rm -f %{buildroot}/usr/include/cpl_conv.h
rm -f %{buildroot}/usr/include/cpl_cpu_features.h
rm -f %{buildroot}/usr/include/cpl_csv.h
rm -f %{buildroot}/usr/include/cpl_error.h
rm -f %{buildroot}/usr/include/cpl_google_cloud.h
rm -f %{buildroot}/usr/include/cpl_hash_set.h
rm -f %{buildroot}/usr/include/cpl_http.h
rm -f %{buildroot}/usr/include/cpl_list.h
rm -f %{buildroot}/usr/include/cpl_minixml.h
rm -f %{buildroot}/usr/include/cpl_minizip_ioapi.h
rm -f %{buildroot}/usr/include/cpl_minizip_unzip.h
rm -f %{buildroot}/usr/include/cpl_minizip_zip.h
rm -f %{buildroot}/usr/include/cpl_multiproc.h
rm -f %{buildroot}/usr/include/cpl_odbc.h
rm -f %{buildroot}/usr/include/cpl_port.h
rm -f %{buildroot}/usr/include/cpl_progress.h
rm -f %{buildroot}/usr/include/cpl_quad_tree.h
rm -f %{buildroot}/usr/include/cpl_sha1.h
rm -f %{buildroot}/usr/include/cpl_sha256.h
rm -f %{buildroot}/usr/include/cpl_spawn.h
rm -f %{buildroot}/usr/include/cpl_string.h
rm -f %{buildroot}/usr/include/cpl_time.h
rm -f %{buildroot}/usr/include/cpl_virtualmem.h
rm -f %{buildroot}/usr/include/cpl_vsi.h
rm -f %{buildroot}/usr/include/cpl_vsi_error.h
rm -f %{buildroot}/usr/include/cpl_vsi_virtual.h
rm -f %{buildroot}/usr/include/cpl_vsil_curl_priv.h
rm -f %{buildroot}/usr/include/cpl_worker_thread_pool.h
rm -f %{buildroot}/usr/include/cplkeywordparser.h
rm -f %{buildroot}/usr/include/gdal.h
rm -f %{buildroot}/usr/include/gdal_alg.h
rm -f %{buildroot}/usr/include/gdal_alg_priv.h
rm -f %{buildroot}/usr/include/gdal_csv.h
rm -f %{buildroot}/usr/include/gdal_frmts.h
rm -f %{buildroot}/usr/include/gdal_mdreader.h
rm -f %{buildroot}/usr/include/gdal_pam.h
rm -f %{buildroot}/usr/include/gdal_priv.h
rm -f %{buildroot}/usr/include/gdal_proxy.h
rm -f %{buildroot}/usr/include/gdal_rat.h
rm -f %{buildroot}/usr/include/gdal_simplesurf.h
rm -f %{buildroot}/usr/include/gdal_utils.h
rm -f %{buildroot}/usr/include/gdal_version.h
rm -f %{buildroot}/usr/include/gdal_vrt.h
rm -f %{buildroot}/usr/include/gdalexif.h
rm -f %{buildroot}/usr/include/gdalgeorefpamdataset.h
rm -f %{buildroot}/usr/include/gdalgrid.h
rm -f %{buildroot}/usr/include/gdalgrid_priv.h
rm -f %{buildroot}/usr/include/gdaljp2abstractdataset.h
rm -f %{buildroot}/usr/include/gdaljp2metadata.h
rm -f %{buildroot}/usr/include/gdaljp2metadatagenerator.h
rm -f %{buildroot}/usr/include/gdalpansharpen.h
rm -f %{buildroot}/usr/include/gdalsse_priv.h
rm -f %{buildroot}/usr/include/gdalwarper.h
rm -f %{buildroot}/usr/include/gdalwarpkernel_opencl.h
rm -f %{buildroot}/usr/include/gnm.h
rm -f %{buildroot}/usr/include/gnm_api.h
rm -f %{buildroot}/usr/include/gnmgraph.h
rm -f %{buildroot}/usr/include/gvgcpfit.h
rm -f %{buildroot}/usr/include/internal_qhull_headers.h
rm -f %{buildroot}/usr/include/memdataset.h
rm -f %{buildroot}/usr/include/ogr_api.h
rm -f %{buildroot}/usr/include/ogr_core.h
rm -f %{buildroot}/usr/include/ogr_feature.h
rm -f %{buildroot}/usr/include/ogr_featurestyle.h
rm -f %{buildroot}/usr/include/ogr_geocoding.h
rm -f %{buildroot}/usr/include/ogr_geometry.h
rm -f %{buildroot}/usr/include/ogr_p.h
rm -f %{buildroot}/usr/include/ogr_spatialref.h
rm -f %{buildroot}/usr/include/ogr_srs_api.h
rm -f %{buildroot}/usr/include/ogrsf_frmts.h
rm -f %{buildroot}/usr/include/rawdataset.h
rm -f %{buildroot}/usr/include/thinplatespline.h
rm -f %{buildroot}/usr/include/vrtdataset.h
rm -f %{buildroot}/usr/lib64/libgdal.so
rm -f %{buildroot}/usr/lib64/pkgconfig/gdal.pc
rm -f %{buildroot}/usr/share/gdal/GDALLogoBW.svg
rm -f %{buildroot}/usr/share/gdal/GDALLogoColor.svg
rm -f %{buildroot}/usr/share/gdal/GDALLogoGS.svg
rm -f %{buildroot}/usr/share/gdal/LICENSE.TXT
rm -f %{buildroot}/usr/share/gdal/compdcs.csv
rm -f %{buildroot}/usr/share/gdal/coordinate_axis.csv
rm -f %{buildroot}/usr/share/gdal/cubewerx_extra.wkt
rm -f %{buildroot}/usr/share/gdal/datum_shift.csv
rm -f %{buildroot}/usr/share/gdal/default.rsc
rm -f %{buildroot}/usr/share/gdal/ecw_cs.wkt
rm -f %{buildroot}/usr/share/gdal/ellipsoid.csv
rm -f %{buildroot}/usr/share/gdal/epsg.wkt
rm -f %{buildroot}/usr/share/gdal/esri_StatePlane_extra.wkt
rm -f %{buildroot}/usr/share/gdal/esri_Wisconsin_extra.wkt
rm -f %{buildroot}/usr/share/gdal/esri_extra.wkt
rm -f %{buildroot}/usr/share/gdal/gcs.csv
rm -f %{buildroot}/usr/share/gdal/gcs.override.csv
rm -f %{buildroot}/usr/share/gdal/gdal_datum.csv
rm -f %{buildroot}/usr/share/gdal/gdalicon.png
rm -f %{buildroot}/usr/share/gdal/gdalvrt.xsd
rm -f %{buildroot}/usr/share/gdal/geoccs.csv
rm -f %{buildroot}/usr/share/gdal/gml_registry.xml
rm -f %{buildroot}/usr/share/gdal/gmlasconf.xml
rm -f %{buildroot}/usr/share/gdal/gmlasconf.xsd
rm -f %{buildroot}/usr/share/gdal/gt_datum.csv
rm -f %{buildroot}/usr/share/gdal/gt_ellips.csv
rm -f %{buildroot}/usr/share/gdal/header.dxf
rm -f %{buildroot}/usr/share/gdal/inspire_cp_BasicPropertyUnit.gfs
rm -f %{buildroot}/usr/share/gdal/inspire_cp_CadastralBoundary.gfs
rm -f %{buildroot}/usr/share/gdal/inspire_cp_CadastralParcel.gfs
rm -f %{buildroot}/usr/share/gdal/inspire_cp_CadastralZoning.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_AdmArea.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_AdmBdry.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_AdmPt.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_BldA.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_BldL.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_Cntr.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_CommBdry.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_CommPt.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_Cstline.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_ElevPt.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_GCP.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_LeveeEdge.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RailCL.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdASL.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdArea.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdCompt.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdEdg.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdMgtBdry.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RdSgmtA.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_RvrMgtBdry.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_SBAPt.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_SBArea.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_SBBdry.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_WA.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_WL.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_WStrA.gfs
rm -f %{buildroot}/usr/share/gdal/jpfgdgml_WStrL.gfs
rm -f %{buildroot}/usr/share/gdal/netcdf_config.xsd
rm -f %{buildroot}/usr/share/gdal/nitf_spec.xml
rm -f %{buildroot}/usr/share/gdal/nitf_spec.xsd
rm -f %{buildroot}/usr/share/gdal/ogrvrt.xsd
rm -f %{buildroot}/usr/share/gdal/osmconf.ini
rm -f %{buildroot}/usr/share/gdal/ozi_datum.csv
rm -f %{buildroot}/usr/share/gdal/ozi_ellips.csv
rm -f %{buildroot}/usr/share/gdal/pci_datum.txt
rm -f %{buildroot}/usr/share/gdal/pci_ellips.txt
rm -f %{buildroot}/usr/share/gdal/pcs.csv
rm -f %{buildroot}/usr/share/gdal/pcs.override.csv
rm -f %{buildroot}/usr/share/gdal/plscenesconf.json
rm -f %{buildroot}/usr/share/gdal/prime_meridian.csv
rm -f %{buildroot}/usr/share/gdal/projop_wparm.csv
rm -f %{buildroot}/usr/share/gdal/ruian_vf_ob_v1.gfs
rm -f %{buildroot}/usr/share/gdal/ruian_vf_st_uvoh_v1.gfs
rm -f %{buildroot}/usr/share/gdal/ruian_vf_st_v1.gfs
rm -f %{buildroot}/usr/share/gdal/ruian_vf_v1.gfs
rm -f %{buildroot}/usr/share/gdal/s57agencies.csv
rm -f %{buildroot}/usr/share/gdal/s57attributes.csv
rm -f %{buildroot}/usr/share/gdal/s57expectedinput.csv
rm -f %{buildroot}/usr/share/gdal/s57objectclasses.csv
rm -f %{buildroot}/usr/share/gdal/seed_2d.dgn
rm -f %{buildroot}/usr/share/gdal/seed_3d.dgn
rm -f %{buildroot}/usr/share/gdal/stateplane.csv
rm -f %{buildroot}/usr/share/gdal/trailer.dxf
rm -f %{buildroot}/usr/share/gdal/unit_of_measure.csv
rm -f %{buildroot}/usr/share/gdal/vdv452.xml
rm -f %{buildroot}/usr/share/gdal/vdv452.xsd
rm -f %{buildroot}/usr/share/gdal/vertcs.csv
rm -f %{buildroot}/usr/share/gdal/vertcs.override.csv

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdal.so.20
/usr/lib64/libgdal.so.20.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-gdal-soname20/0cd23537e3c32497c7b87157b36f9d2eb5fca64b
/usr/share/package-licenses/compat-gdal-soname20/1d982db70b88f943cc7d15013c28a126339d6cbc
/usr/share/package-licenses/compat-gdal-soname20/1f906240d40bc72f70c6765ed4df959defd3c153
/usr/share/package-licenses/compat-gdal-soname20/3035b519169390d1aaa3a43267deaae5cdff8a9b
/usr/share/package-licenses/compat-gdal-soname20/3c5056c99522acf3d9e2c2a2f61fdeeffced4174
/usr/share/package-licenses/compat-gdal-soname20/baf1d15dcf66b1e1dfee80eb405aa73105842017
/usr/share/package-licenses/compat-gdal-soname20/df97bdf33b01f9ed42a799dd3ed7a1599dd0cb9d
/usr/share/package-licenses/compat-gdal-soname20/f7f1d88d0aea6c567a2c351b08b0fe80f2582054
/usr/share/package-licenses/compat-gdal-soname20/f9c9a2d3495a0766b4cf20d4b90cfe714dab3dc1
