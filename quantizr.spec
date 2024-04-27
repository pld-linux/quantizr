Summary:	Fast library for converting RGBA images to 8-bit palette images
Summary(pl.UTF-8):	Szybka biblioteka do konwersji obrazów RGBA do obrazów 8-bitowych z paletą
Name:		quantizr
Version:	1.4.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/DarthSim/quantizr/releases
Source0:	https://github.com/DarthSim/quantizr/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c39ed3268502ba531641d64f24b7e7c4
URL:		https://github.com/DarthSim/quantizr
BuildRequires:	cargo
BuildRequires:	cargo-c
BuildRequires:	rust
BuildRequires:	rpmbuild(macros) >= 2.012
ExclusiveArch:	%{rust_arches}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Fast library for converting RGBA images to 8-bit palette images.

%description -l pl.UTF-8
Szybka biblioteka do konwersji obrazów RGBA do obrazów 8-bitowych z
paletą.

%package devel
Summary:	Header files for quantizr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki quantizr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for quantizr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki quantizr.

%package static
Summary:	Static quantizr library
Summary(pl.UTF-8):	Statyczna biblioteka quantizr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static quantizr library.

%description static -l pl.UTF-8
Statyczna biblioteka quantizr.

%prep
%setup -q

%build
cargo -v cbuild --offline --release --target %{rust_target} \
	--prefix %{_prefix} \
	--libdir %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

cargo -v cinstall --frozen --release --target %{rust_target} \
	--destdir $RPM_BUILD_ROOT \
	--prefix %{_prefix} \
	--includedir %{_includedir} \
	--libdir %{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libquantizr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libquantizr.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libquantizr.so
%{_includedir}/quantizr
%{_pkgconfigdir}/quantizr.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libquantizr.a
