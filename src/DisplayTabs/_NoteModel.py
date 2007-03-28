#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id: _NoteModel.py 7068 2006-07-24 23:06:49Z rshura $

#-------------------------------------------------------------------------
#
# GTK libraries
#
#-------------------------------------------------------------------------
import gtk

#-------------------------------------------------------------------------
#
# NoteModel
#
#-------------------------------------------------------------------------
class NoteModel(gtk.ListStore):

    def __init__(self, note_list, db):
        gtk.ListStore.__init__(self, str, str, object)
        self.db = db
        for handle in note_list:
            note = self.db.get_note_from_handle(handle)
            text = note.get().replace('\n', ' ')
            if len(text) > 80:
                text = text[:80]+"..."
            self.append(row=[
                str(note.get_type()), 
                text, 
                handle, 
                ])
