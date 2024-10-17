Name:		texlive-context-simplefonts
Version:	47085
Release:	2
Summary:	Simplified font usage for ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-simplefonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simplefonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simplefonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package defines a set of commands for loading and using
fonts in ConTeXt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/simplefonts
%doc %{_texmfdistdir}/doc/context/third/simplefonts

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
