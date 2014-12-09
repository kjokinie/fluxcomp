Name:       fluxcomp
Summary:    Direct FB flux interface definition compiler
Version:    1.4.4
Release:    1
Group:      Development/Tools
License:    MIT
URL:        http://directfb.org/
Source0:    %{name}-%{version}.tar.bz2

%description
Fluxcomp is a tool for compiling Direct FB .flux interface definition files
into .c and .cpp files. It is used in when compiling the Direct FB library.

%prep
%setup -q -n %{name}-%{version}

%build

pushd fluxcomp
%autogen
%configure
make %{?jobs:-j%jobs}
popd

%install
rm -rf %{buildroot}
pushd fluxcomp
%make_install
popd

%files
%defattr(755,root,root,-)
%{_bindir}/*
